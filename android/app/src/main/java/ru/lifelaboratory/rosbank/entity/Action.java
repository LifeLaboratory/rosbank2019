package ru.lifelaboratory.rosbank.entity;

import com.google.gson.annotations.SerializedName;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

/**
 * Сущность активности пользователя
 * @author Boris Bockarev <Boris-Bochkaryov@yandex.ru>
 */
@NoArgsConstructor
@AllArgsConstructor
@Getter
@Setter
public class Action {

    @SerializedName("id_user")
    private Integer idUser;
    @SerializedName("id_action")
    private Integer idAction;
    private String platform;

}
