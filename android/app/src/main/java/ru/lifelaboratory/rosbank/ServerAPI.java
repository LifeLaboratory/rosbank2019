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

/**
 * Интерфейс для взаимодействия с сервером
 * @author Boris Bockarev <Boris-Bochkaryov@yandex.ru>
 * @see retrofit2.Retrofit
 */
public interface ServerAPI {

    /**
     * Метод для отправки действий пользователя на сервер
     * @param action - объект действия
     * @return объект пользователя
     * @see Action
     */
    @POST("/api/statistic")
    Call<User> addToStatistic(@Body Action action);

    /**
     * Метод для авторизации пользователя
     * @param user - объект пользователя, с заполненными логином и паролем
     * @return заполненный объект пользователя
     * @see User
     */
    @POST("/api/auth")
    Call<User> auth(@Body User user);

    /**
     * Метод для получения сторис, преднозначенных пользователю
     * @param id - идендификатор пользователя
     * @return список с заполненными объектами сторис
     * @see Stories
     */
    @GET("/api/stories/{id_user}?type=1")
    Call<List<Stories>> getStories(@Path("id_user") Integer id);

    /**
     * Метод для получения нотификаций, преднозначенных пользователю
     * @param id - идендификатор пользователя
     * @return список с заполненными объектами уведомлений
     * @see Notification
     */
    @GET("/api/notifications/{id_user}")
    Call<List<Notification>> getNotification(@Path("id_user") Integer id);

    /**
     * Метод для отправки информации о статусе просмотра историй
     * @param id - объект статуса просмотра с заполненым идентификатором пользователя и типом события
     * @return заглушка
     * @see ViewStories
     */
    @POST("/api/stories/update_status")
    Call<Object> sendView(@Body ViewStories id);

}
