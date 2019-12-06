package ru.lifelaboratory.rosbank;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

public class CurrencyTransferActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_currency_transfer);

        ((Button) findViewById(R.id.btn_convert)).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Toast.makeText(CurrencyTransferActivity.this, "Конвертирование осуществлено", Toast.LENGTH_SHORT).show();
            }
        });
    }
}
