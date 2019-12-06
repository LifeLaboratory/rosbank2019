package ru.lifelaboratory.rosbank;

import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.POST;

public interface ServerAPI {

    @POST("/api/statistic")
    void addToStatistic(@Body Action action);

    @POST("/api/auth")
    Call<User> auth(@Body User user);

}
