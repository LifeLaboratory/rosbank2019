package ru.lifelaboratory.rosbank;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.graphics.Color;
import android.support.annotation.NonNull;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.Toast;

import com.rahuljanagouda.statusstories.StatusStoriesActivity;
import com.squareup.picasso.Picasso;
import com.tooltip.OnClickListener;
import com.tooltip.Tooltip;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;
import ru.lifelaboratory.rosbank.entity.Action;
import ru.lifelaboratory.rosbank.entity.Stories;
import ru.lifelaboratory.rosbank.entity.User;
import ru.lifelaboratory.rosbank.entity.ViewStories;

public class MainActivity extends AppCompatActivity {

    public static Retrofit server;
    public static User user;

    {
        server = new Retrofit.Builder()
                .addConverterFactory(GsonConverterFactory.create())
                .baseUrl("http://100.64.17.109:13451/")
                .build();
    }

    static public Integer[] idResources = null;

    public String[] resources = null;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        SharedPreferences sharedPreferences = getSharedPreferences("ROSBANK2019", Context.MODE_PRIVATE);
        if (sharedPreferences.getInt("id", -1) == -1) {
            setContentView(R.layout.activity_main_without_login);

            ((Button) findViewById(R.id.btn_auth)).setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {

                    ServerAPI auth = MainActivity.server.create(ServerAPI.class);
                    User user = new User();
                    user.setLogin(((EditText) findViewById(R.id.login)).getText().toString());
                    user.setPassword(((EditText) findViewById(R.id.password)).getText().toString());
                    auth.auth(user)
                            .enqueue(new Callback<User>() {
                                @Override
                                public void onResponse(Call<User> call, Response<User> response) {
                                    if (response.body().getMessage() != null) {
                                        Toast.makeText(MainActivity.this, "Неверный логин или пароль", Toast.LENGTH_SHORT).show();
                                    } else {
                                        Toast.makeText(MainActivity.this, "Авторизация удачна", Toast.LENGTH_SHORT).show();
                                        SharedPreferences sharedPreferences = getSharedPreferences("ROSBANK2019", Context.MODE_PRIVATE);
                                        sharedPreferences.edit()
                                                .putString("login", ((EditText) findViewById(R.id.login)).getText().toString())
                                                .putString("password", ((EditText) findViewById(R.id.login)).getText().toString())
                                                .putInt("id", response.body().getIdUser())
                                                .apply();
                                        MainActivity.user = new User();
                                        MainActivity.user.setIdUser(response.body().getIdUser());
                                        MainActivity.user.setLogin(((EditText) findViewById(R.id.login)).getText().toString());
                                        MainActivity.user.setPassword(((EditText) findViewById(R.id.password)).getText().toString());
                                        startActivity(new Intent(MainActivity.this, MainActivity.class));
                                    }
                                }

                                @Override
                                public void onFailure(Call<User> call, Throwable t) {

                                }
                            });
                }
            });
        } else {
            startService(new Intent(MainActivity.this, NotificationService.class));

            MainActivity.user = new User();
            MainActivity.user.setIdUser(sharedPreferences.getInt("id", -1));
            MainActivity.user.setLogin(sharedPreferences.getString("login", ""));
            MainActivity.user.setPassword(sharedPreferences.getString("password", ""));

            setContentView(R.layout.activity_main);

            ServerAPI auth = MainActivity.server.create(ServerAPI.class);
            auth.getStories(MainActivity.user.getIdUser())
                    .enqueue(new Callback<List<Stories>>() {
                        @Override
                        public void onResponse(Call<List<Stories>> call, Response<List<Stories>> response) {
                            if (response.body() != null) {
                                List<String> tmp = new ArrayList<>();
                                List<Integer> tmpInteger = new ArrayList<>();
                                for (int i = 0; i < response.body().size(); i++) {
                                    for (int j = 0; j < response.body().get(i).getImage().size(); j++) {
                                        Log.e("ROSBNAK2019", response.body().get(i).getImage().get(j));
                                        ImageView img = new ImageView(MainActivity.this);
                                        LinearLayout.LayoutParams lp = new LinearLayout.LayoutParams(LinearLayout.LayoutParams.WRAP_CONTENT, LinearLayout.LayoutParams.MATCH_PARENT);
                                        lp.setMargins(32, 32, 32, 32);
                                        img.setLayoutParams(lp);
                                        img.setScaleType(ImageView.ScaleType.CENTER_CROP);
                                        Picasso.with(MainActivity.this)
                                                .load(response.body().get(i).getImage().get(j))
                                                .placeholder(R.drawable.tmp)
                                                .error(R.drawable.tmp)
                                                .into(img);
                                        ((LinearLayout) findViewById(R.id.list_stories)).addView(img);
                                        tmp.add(response.body().get(i).getImage().get(j));
                                        tmpInteger.add(response.body().get(i).getId());
                                    }
                                }
                                resources = new String[tmp.size()];
                                idResources = new Integer[tmp.size()];
                                tmp.toArray(resources);
                                tmpInteger.toArray(idResources);
                            }
                        }

                        @Override
                        public void onFailure(Call<List<Stories>> call, Throwable t) {
                        }
                    });

            ((LinearLayout) findViewById(R.id.list_stories)).setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    ServerAPI auth = MainActivity.server.create(ServerAPI.class);
                    for (int i = 0; i < idResources.length; i++) {
                        ViewStories viewStories = new ViewStories();
                        viewStories.setIdUser(MainActivity.user.getIdUser());
                        viewStories.setIdStories(idResources[i]);
                        viewStories.setStatus("open");
                        auth.sendView(viewStories)
                                .enqueue(new Callback<Object>() {
                                    @Override
                                    public void onResponse(Call<Object> call, Response<Object> response) {
                                    }

                                    @Override
                                    public void onFailure(Call<Object> call, Throwable t) {
                                        Log.e("ROSBANK2019", t.getMessage());
                                    }
                                });
                    }
                    Intent a = new Intent(MainActivity.this, StatusStoriesActivity.class);
                    a.putExtra(StatusStoriesActivity.STATUS_RESOURCES_KEY, resources);
                    a.putExtra(StatusStoriesActivity.STATUS_DURATION_KEY, 3000L);
                    a.putExtra(StatusStoriesActivity.IS_IMMERSIVE_KEY, true);
                    a.putExtra(StatusStoriesActivity.IS_CACHING_ENABLED_KEY, true);
                    a.putExtra(StatusStoriesActivity.IS_TEXT_PROGRESS_ENABLED_KEY, true);
                    startActivity(a);
                }
            });

            // к переводам
            ((LinearLayout) findViewById(R.id.to_transfer)).setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    startActivity(new Intent(MainActivity.this, TransferActivity.class));
                }
            });

            // к конвертированию
            ((LinearLayout) findViewById(R.id.to_currency_transfer)).setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    startActivity(new Intent(MainActivity.this, CurrencyTransferActivity.class));
                }
            });

            // к QR
            ((LinearLayout) findViewById(R.id.to_qr_payment)).setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    ServerAPI auth = MainActivity.server.create(ServerAPI.class);
                    Action action = new Action();
                    action.setIdUser(MainActivity.user.getIdUser());
                    action.setIdAction(3); // переход к переводам
                    action.setPlatform("android");
                    auth.addToStatistic(action)
                            .enqueue(new Callback<User>() {
                                @Override
                                public void onResponse(Call<User> call, Response<User> response) {
                                }

                                @Override
                                public void onFailure(Call<User> call, Throwable t) {
                                }
                            });
                    startActivity(new Intent(MainActivity.this, QRPaymentActivity.class));
                }
            });

            Intent intent = getIntent();
            String link = intent.getDataString();
            if (link != null) {
                Log.e("ROSBANK2019", link);
                if (link.split("/")[link.split("/").length - 1].equals("convert")) {
                    startActivity(new Intent(MainActivity.this, CurrencyTransferActivity.class));
                } else if(link.split("/")[link.split("/").length - 1].equals("transfer")) {
                    startActivity(new Intent(MainActivity.this, TransferActivity.class));
                } else if(link.split("/")[link.split("/").length - 1].equals("qr")){
                    startActivity(new Intent(MainActivity.this, QRPaymentActivity.class));
                }
            }
        }
    }

    List<String> image = new ArrayList<>();
    List<String> description = new ArrayList<>();

    @Override
    protected void onResume() {
        super.onResume();

        Intent intent = getIntent();
        String action = intent.getAction();
        if (action != null) {
            Log.e("ROSBANK2019", action);
            if (action.equals("android.intent.action.MAIN")) {
                ServerAPI auth = MainActivity.server.create(ServerAPI.class);
                if (idResources != null)
                    for (int i = 0; i < idResources.length; i++) {
                        ViewStories viewStories = new ViewStories();
                        viewStories.setIdUser(MainActivity.user.getIdUser());
                        viewStories.setIdStories(idResources[i]);
                        viewStories.setStatus("view");
                        auth.sendView(viewStories)
                                .enqueue(new Callback<Object>() {
                                    @Override
                                    public void onResponse(Call<Object> call, Response<Object> response) { }

                                    @Override
                                    public void onFailure(Call<Object> call, Throwable t) {
                                        Log.e("ROSBANK2019", t.getMessage());
                                    }
                                });
                    }
            } else if(action.equals("lifelaboratory.from_notification_service")) {

                if (intent.getIntExtra("TYPE", -1) == 2) {
                    Collections.addAll(image, intent.getStringExtra("image").split(";"));
                    Collections.addAll(description, intent.getStringExtra("description").split(";"));

                    int resID = getResources().getIdentifier(image.get(0), "id", getPackageName());
                    if (findViewById(resID) != null) {
                        new Tooltip.Builder(findViewById(resID))
                                .setBackgroundColor(Color.parseColor("#000000"))
                                .setTextColor(Color.parseColor("#ffffff"))
                                .setTextSize(25.0f)
                                .setArrowHeight(50.0f)
                                .setArrowWidth(50.0f)
                                .setOnClickListener(new OnClickListener() {
                                    @Override
                                    public void onClick(@NonNull Tooltip tooltip) {
                                        tooltip.dismiss();
                                        if (image.size() > 0) {
                                            image.remove(0);
                                            description.remove(0);
                                            StringBuilder imageString = new StringBuilder();
                                            StringBuilder descriptionString = new StringBuilder();
                                            for (int j = 0; j < image.size(); j++) {
                                                imageString.append(image.get(j)).append(";");
                                                descriptionString.append(description.get(j)).append(";");
                                            }
                                            startActivity(new Intent(MainActivity.this, MainActivity.class)
                                                    .setAction("lifelaboratory.from_notification_service")
                                                    .putExtra("TYPE", 2)
                                                    .putExtra("image", imageString.toString())
                                                    .putExtra("description", descriptionString.toString()));
                                            overridePendingTransition(0, 0);
                                        }
                                    }
                                })
                                .setText(description.get(0)).show();
                    }
                }
            }
        }
    }

}