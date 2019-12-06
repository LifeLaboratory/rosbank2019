package ru.lifelaboratory.rosbank;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.Toast;

import com.rahuljanagouda.statusstories.StatusStoriesActivity;

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
                .baseUrl("http://dc991e59.ngrok.io/")
                .build();
    }

    private final String[] resources = new String[]{
            "https://firebasestorage.googleapis.com/v0/b/firebase-satya.appspot.com/o/images%2Fi00001.jpg?alt=media&token=460667e4-e084-4dc5-b873-eefa028cec32",
            "https://firebasestorage.googleapis.com/v0/b/firebase-satya.appspot.com/o/images%2Fi00002.jpg?alt=media&token=e8e86192-eb5d-4e99-b1a8-f00debcdc016",
            "https://firebasestorage.googleapis.com/v0/b/firebase-satya.appspot.com/o/images%2Fi00004.jpg?alt=media&token=af71cbf5-4be3-4f8a-8a2b-2994bce38377",
            "https://firebasestorage.googleapis.com/v0/b/firebase-satya.appspot.com/o/images%2Fi00005.jpg?alt=media&token=7d179938-c419-44f4-b965-1993858d6e71",
            "https://firebasestorage.googleapis.com/v0/b/firebase-satya.appspot.com/o/images%2Fi00006.jpg?alt=media&token=cdd14cf5-6ed0-4fb7-95f5-74618528a48b",
            "https://firebasestorage.googleapis.com/v0/b/firebase-satya.appspot.com/o/images%2Fi00007.jpg?alt=media&token=98524820-6d7c-4fb4-89b1-65301e1d6053",
            "https://firebasestorage.googleapis.com/v0/b/firebase-satya.appspot.com/o/images%2Fi00008.jpg?alt=media&token=7ef9ed49-3221-4d49-8fb4-2c79e5dab333",
            "https://firebasestorage.googleapis.com/v0/b/firebase-satya.appspot.com/o/images%2Fi00009.jpg?alt=media&token=00d56a11-7a92-4998-a05a-e1dd77b02fe4",
            "https://firebasestorage.googleapis.com/v0/b/firebase-satya.appspot.com/o/images%2Fi00010.jpg?alt=media&token=24f8f091-acb9-432a-ae0f-7e6227d18803",
    };

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        SharedPreferences sharedPreferences = getSharedPreferences("ROSBANK2019", Context.MODE_PRIVATE);
        if(sharedPreferences.getInt("id", -1) == -1){
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

            MainActivity.user = new User()
                    .setIdUser(sharedPreferences.getInt("id", -1))
                    .setLogin(sharedPreferences.getString("login", ""))
                    .setPassword(sharedPreferences.getString("password", ""));

            setContentView(R.layout.activity_main);

            ((ImageView) findViewById(R.id.tmp_img)).setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
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
                                public void onResponse(Call<User> call, Response<User> response) { }
                                @Override
                                public void onFailure(Call<User> call, Throwable t) { }
                            });
                    startActivity(new Intent(MainActivity.this, QRPaymentActivity.class));
                }
            });
        }
    }
}
