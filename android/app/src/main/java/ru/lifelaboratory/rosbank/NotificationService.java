package ru.lifelaboratory.rosbank;

import android.app.NotificationManager;
import android.app.PendingIntent;
import android.app.Service;
import android.content.Intent;
import android.os.IBinder;
import android.support.v4.app.NotificationCompat;
import android.util.Log;

import java.util.List;
import java.util.concurrent.TimeUnit;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import ru.lifelaboratory.rosbank.entity.Notification;
import ru.lifelaboratory.rosbank.util.Constants;

/**
 * Фоновый сервис, предназначенный для уведомления
 * @author Boris Bockarev <Boris-Bochkaryov@yandex.ru>
 * @see Notification
 * @see Service
 */
public class NotificationService extends Service {

    public int onStartCommand(Intent intent, int flags, int startId) {
        // отдельный поток для постоянного взаимодействия с сервером
        new Thread(new Runnable() {
            public void run() {
                while(true) {
                    if (MainActivity.server != null) { // сервис не работает, если пользователь вывел приложение из памяти
                        // получение уведомлений
                        ServerAPI notification = MainActivity.server.create(ServerAPI.class);
                        notification.getNotification(MainActivity.user.getIdUser())
                                .enqueue(new Callback<List<Notification>>() {
                                    @Override
                                    public void onResponse(Call<List<Notification>> call, Response<List<Notification>> response) {
                                        if (response.body() != null) {
                                            for (int i = 0; i < response.body().size(); i++) {
                                                Log.d(Constants.LOG_TAG, "Текст уведомления: " + response.body().get(i).getName());
                                                Intent toMainActivity = new Intent(getApplicationContext(), MainActivity.class)
                                                        .setAction(Constants.INTENT_ACTION);
                                                // если тип уведомления - интерактивный туториал
                                                if (response.body().get(i).getType() != null && response.body().get(i).getType().equals(2)) {
                                                    toMainActivity.putExtra("TYPE", 2);
                                                    StringBuilder image = new StringBuilder();
                                                    StringBuilder description = new StringBuilder();
                                                    for (int j = 0; j < response.body().get(i).getImage().size(); j++){
                                                        image.append(response.body().get(i).getImage().get(j)).append(";");
                                                        description.append(response.body().get(i).getDescription().get(j)).append(";");
                                                    }
                                                    toMainActivity.putExtra("image", image.toString());
                                                    toMainActivity.putExtra("description", description.toString());
                                                }

                                                // сборка уведомления
                                                PendingIntent contentIntent = PendingIntent.getActivity(getApplicationContext(), 0,
                                                        toMainActivity, PendingIntent.FLAG_UPDATE_CURRENT);
                                                NotificationCompat.Builder builder =
                                                        new NotificationCompat.Builder(getApplicationContext())
                                                                .setSmallIcon(R.mipmap.ic_launcher)
                                                                .setContentTitle(response.body().get(i).getName())
                                                                .setContentText(response.body().get(i).getUrl())
                                                                .setContentIntent(contentIntent);
                                                android.app.Notification notification = builder.build();
                                                NotificationManager notificationManager =
                                                        (NotificationManager) getSystemService(NOTIFICATION_SERVICE);

                                                notificationManager.notify(1, notification);
                                            }
                                        }
                                    }

                                    @Override
                                    public void onFailure(Call<List<Notification>> call, Throwable t) {
                                        Log.e(Constants.LOG_TAG, "Error from NotificationService: " + t.getMessage());
                                    }
                                });
                        try {
                            TimeUnit.SECONDS.sleep(10);
                        } catch (InterruptedException e) {
                            Log.e(Constants.LOG_TAG, e.getMessage());
                        }
                    } else {
                        break;
                    }
                }
            }
        }).start();
        return super.onStartCommand(intent, flags, startId);
    }

    @Override
    public IBinder onBind(Intent intent) {
        return null;
    }
}
