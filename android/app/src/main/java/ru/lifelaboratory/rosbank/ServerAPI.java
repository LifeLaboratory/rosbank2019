package ru.lifelaboratory.rosbank;

import java.util.List;

import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.GET;
import retrofit2.http.POST;
import retrofit2.http.Path;
import ru.lifelaboratory.rosbank.entity.Action;
import ru.lifelaboratory.rosbank.entity.Notification;
import ru.lifelaboratory.rosbank.entity.Stories;
import ru.lifelaboratory.rosbank.entity.User;
import ru.lifelaboratory.rosbank.entity.ViewStories;

public interface ServerAPI {

    @POST("/api/statistic")
    Call<User> addToStatistic(@Body Action action);

    @POST("/api/auth")
    Call<User> auth(@Body User user);

    @GET("/api/stories/{id_user}?type=1")
    Call<List<Stories>> getStories(@Path("id_user") Integer id);

    @GET("/api/notifications/{id_user}")
    Call<List<Notification>> getNotification(@Path("id_user") Integer id);

    @POST("/api/stories/update_status")
    Call<Object> sendView(@Body ViewStories id);

}
