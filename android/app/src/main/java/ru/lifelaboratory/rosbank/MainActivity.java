package ru.lifelaboratory.rosbank;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.DisplayMetrics;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.ListView;
import android.widget.Toast;

import com.rahuljanagouda.statusstories.StatusStoriesActivity;
import com.squareup.picasso.Picasso;

import java.util.ArrayList;
import java.util.List;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

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

    public String[] resources = null; //new String[]{
//            "https://firebasestorage.googleapis.com/v0/b/firebase-satya.appspot.com/o/images%2Fi00001.jpg?alt=media&token=460667e4-e084-4dc5-b873-eefa028cec32",
//            "https://firebasestorage.googleapis.com/v0/b/firebase-satya.appspot.com/o/images%2Fi00002.jpg?alt=media&token=e8e86192-eb5d-4e99-b1a8-f00debcdc016",
//            "https://firebasestorage.googleapis.com/v0/b/firebase-satya.appspot.com/o/images%2Fi00004.jpg?alt=media&token=af71cbf5-4be3-4f8a-8a2b-2994bce38377",
//            "https://firebasestorage.googleapis.com/v0/b/firebase-satya.appspot.com/o/images%2Fi00005.jpg?alt=media&token=7d179938-c419-44f4-b965-1993858d6e71",
//            "https://firebasestorage.googleapis.com/v0/b/firebase-satya.appspot.com/o/images%2Fi00006.jpg?alt=media&token=cdd14cf5-6ed0-4fb7-95f5-74618528a48b",
//            "https://firebasestorage.googleapis.com/v0/b/firebase-satya.appspot.com/o/images%2Fi00007.jpg?alt=media&token=98524820-6d7c-4fb4-89b1-65301e1d6053",
//            "https://firebasestorage.googleapis.com/v0/b/firebase-satya.appspot.com/o/images%2Fi00008.jpg?alt=media&token=7ef9ed49-3221-4d49-8fb4-2c79e5dab333",
//            "https://firebasestorage.googleapis.com/v0/b/firebase-satya.appspot.com/o/images%2Fi00009.jpg?alt=media&token=00d56a11-7a92-4998-a05a-e1dd77b02fe4",
//            "https://firebasestorage.googleapis.com/v0/b/firebase-satya.appspot.com/o/images%2Fi00010.jpg?alt=media&token=24f8f091-acb9-432a-ae0f-7e6227d18803",
//    };

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
                    auth.auth(
                            new User()
                                    .setLogin(((EditText) findViewById(R.id.login)).getText().toString())
                                    .setPassword(((EditText) findViewById(R.id.password)).getText().toString()))
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
                                        MainActivity.user = new User()
                                                .setIdUser(response.body().getIdUser())
                                                .setLogin(((EditText) findViewById(R.id.login)).getText().toString())
                                                .setPassword(((EditText) findViewById(R.id.password)).getText().toString());
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

            MainActivity.user = new User()
                    .setIdUser(sharedPreferences.getInt("id", -1))
                    .setLogin(sharedPreferences.getString("login", ""))
                    .setPassword(sharedPreferences.getString("password", ""));

            setContentView(R.layout.activity_main);

            ServerAPI auth = MainActivity.server.create(ServerAPI.class);
            auth.getStories(MainActivity.user.getIdUser())
                    .enqueue(new Callback<List<Stories>>() {
                        @Override
                        public void onResponse(Call<List<Stories>> call, Response<List<Stories>> response) {
                            List<String> tmp = new ArrayList<>();
                            List<Integer> tmpInteger = new ArrayList<>();
                            for (int i = 0; i < response.body().size(); i++) {
                                for (int j = 0; j < response.body().get(i).getImage().size(); j++) {
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

                        @Override
                        public void onFailure(Call<List<Stories>> call, Throwable t) {
                        }
                    });

            ((LinearLayout) findViewById(R.id.list_stories)).setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    ServerAPI auth = MainActivity.server.create(ServerAPI.class);
                    for (int i = 0; i < idResources.length; i++) {
                        auth.sendView(new ViewStories()
                                .setIdUser(MainActivity.user.getIdUser())
                                .setIdStories(idResources[i])
                                .setStatus("open"))
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
                    auth.addToStatistic(new Action()
                            .setIdUser(MainActivity.user.getIdUser())
                            .setIdAction(3) // переход к переводам
                            .setPlatform("ANDROID"))
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
        }
    }

    @Override
    protected void onResume() {
        super.onResume();

        Intent intent = getIntent();
        String action = intent.getAction();
        Log.e("ROSBANK2019", action);
        if (action.equals("android.intent.action.MAIN")) {
            ServerAPI auth = MainActivity.server.create(ServerAPI.class);
            if (idResources != null)
                for (int i = 0; i < idResources.length; i++) {
                    auth.sendView(new ViewStories()
                            .setIdUser(MainActivity.user.getIdUser())
                            .setIdStories(idResources[i])
                            .setStatus("view"))
                            .enqueue(new Callback<Object>() {
                                @Override
                                public void onResponse(Call<Object> call, Response<Object> response) { }
                                @Override
                                public void onFailure(Call<Object> call, Throwable t) {
                                    Log.e("ROSBANK2019", t.getMessage());
                                }
                            });
                }
        }
    }
}