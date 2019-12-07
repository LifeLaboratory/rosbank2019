package ru.lifelaboratory.rosbank.entity;

import com.google.gson.annotations.SerializedName;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

/**
 * Сущность статуса просмотра сторис
 * @author Boris Bockarev <Boris-Bochkaryov@yandex.ru>
 */
@NoArgsConstructor
@AllArgsConstructor
@Setter
@Getter
public class ViewStories {

    @SerializedName("id_user")
    private Integer idUser;
    @SerializedName("id_stories")
    private Integer idStories;
    private String status;

}
