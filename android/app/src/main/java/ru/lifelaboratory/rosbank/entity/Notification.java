package ru.lifelaboratory.rosbank.entity;

import com.google.gson.annotations.SerializedName;

import java.util.List;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

/**
 * Сущность уведомления
 * @author Boris Bockarev <Boris-Bochkaryov@yandex.ru>
 */
@NoArgsConstructor
@AllArgsConstructor
@Setter
@Getter
public class Notification {

    @SerializedName("id_notification")
    private Integer id;
    private String name;
    private String url;
    private List<String> image;
    private List<String> description;
    private Integer type;

}
