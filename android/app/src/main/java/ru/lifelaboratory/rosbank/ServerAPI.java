package ru.lifelaboratory.rosbank;

import java.util.List;

import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.GET;
import retrofit2.http.POST;
import retrofit2.http.Path;

public interface ServerAPI {

    @POST("/api/statistic")
    Call<User> addToStatistic(@Body Action action);

    @POST("/api/auth")
    Call<User> auth(@Body User user);

    @GET("/api/stories/{id_user}")
    Call<List<Stories>> getStories(@Path("id_user") Integer id);

    @GET("/api/notifications/{id_user}")
    Call<List<Notification>> getNotification(@Path("id_user") Integer id);

    @POST("/api/stories/view")
    Call<Object> sendView(@Body ViewStories id);

}
