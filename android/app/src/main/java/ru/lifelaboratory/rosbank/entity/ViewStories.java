package ru.lifelaboratory.rosbank.entity;

import com.google.gson.annotations.SerializedName;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

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
