package ru.lifelaboratory.rosbank.entity;

import com.google.gson.annotations.SerializedName;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

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
