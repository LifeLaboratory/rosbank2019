package ru.lifelaboratory;

import io.vertx.core.Vertx;
import io.vertx.core.VertxOptions;
import io.vertx.core.eventbus.EventBus;
import io.vertx.core.eventbus.MessageConsumer;
import io.vertx.core.http.HttpClient;
import io.vertx.core.http.HttpClientOptions;
import io.vertx.core.http.HttpMethod;
import io.vertx.core.http.HttpVersion;

public class Application {

    public static void main(String[] args) {
        Vertx vertx = Vertx.vertx();

        vertx.createHttpServer().requestHandler(request -> {
            if (request.uri().equals("/"))
                request.response().sendFile("html/index.html");
            else if (request.uri().equals("/profile"))
                request.response().sendFile("html/profile.html");
            else if (request.uri().equals("/transfer"))
                request.response().sendFile("html/transfer.html");
            else if (request.uri().equals("/convert"))
                request.response().sendFile("html/convert.html");
            else if (request.uri().equals("/qr"))
                request.response().sendFile("html/qr.html");
            else if (!request.uri().equals("/favicon.ico"))
                request.response().sendFile(request.uri().substring(1));
            else
                request.response().end();
        }).listen(8081);
    }

}
