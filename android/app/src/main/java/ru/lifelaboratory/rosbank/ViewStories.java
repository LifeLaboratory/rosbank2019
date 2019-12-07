package ru.lifelaboratory.rosbank;

import com.google.gson.annotations.SerializedName;

public class ViewStories {

    @SerializedName("id_user")
    private Integer idUser;
    @SerializedName("id_stories")
    private Integer idStories;
    private String status;


    public Integer getIdUser() {
        return idUser;
    }

    public ViewStories setIdUser(Integer idUser) {
        this.idUser = idUser;
        return this;
    }

    public Integer getIdStories() {
        return idStories;
    }

    public ViewStories setIdStories(Integer idStories) {
        this.idStories = idStories;
        return this;
    }

    public String getStatus() {
        return status;
    }

    public ViewStories setStatus(String status) {
        this.status = status;
        return this;
    }
}
