package ru.lifelaboratory.rosbank.entity;

import com.google.gson.annotations.SerializedName;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

/**
 * Сущность пользователя
 * @author Boris Bockarev <Boris-Bochkaryov@yandex.ru>
 */
@NoArgsConstructor
@AllArgsConstructor
@Getter
@Setter
public class User {

    private String login;
    private String password;
    @SerializedName("id_user")
    private Integer idUser;
    private String message;

}