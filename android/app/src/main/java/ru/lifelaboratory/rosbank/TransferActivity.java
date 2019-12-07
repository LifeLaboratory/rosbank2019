package ru.lifelaboratory.rosbank;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import ru.lifelaboratory.rosbank.entity.Action;
import ru.lifelaboratory.rosbank.entity.User;

public class TransferActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_transfer);


        ((Button) findViewById(R.id.btn_send)).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                ServerAPI auth = MainActivity.server.create(ServerAPI.class);
                Action action = new Action();
                action.setIdUser(MainActivity.user.getIdUser());
                action.setIdAction(1); // переход к конвертации
                action.setPlatform("android");
                auth.addToStatistic(action)
                        .enqueue(new Callback<User>() {
                            @Override
                            public void onResponse(Call<User> call, Response<User> response) { }
                            @Override
                            public void onFailure(Call<User> call, Throwable t) { }
                        });
                Toast.makeText(TransferActivity.this, "Перевод осуществлен", Toast.LENGTH_SHORT).show();
            }
        });
    }
}
