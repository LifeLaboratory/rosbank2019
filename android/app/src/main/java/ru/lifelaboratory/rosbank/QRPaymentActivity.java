package ru.lifelaboratory.rosbank;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;

/**
 * Класс для экрана "Оплата по QR-коду"
 * @author Boris Bockarev <Boris-Bochkaryov@yandex.ru>
 */
public class QRPaymentActivity extends AppCompatActivity {

    /**
     * Создание активности
     * @param savedInstanceState
     */
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_qr_payment);
    }
}
