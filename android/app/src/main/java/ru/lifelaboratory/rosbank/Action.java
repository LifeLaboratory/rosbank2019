package ru.lifelaboratory.rosbank;

import com.google.gson.annotations.SerializedName;

public class Action {

    @SerializedName("id_user")
    private Integer idUser;
    @SerializedName("id_action")
    private Integer idAction;
    private String platform;

    public Integer getIdUser() {
        return idUser;
    }

    public Action setIdUser(Integer idUser) {
        this.idUser = idUser;
        return this;
    }

    public Integer getIdAction() {
        return idAction;
    }

    public Action setIdAction(Integer idAction) {
        this.idAction = idAction;
        return this;
    }

    public String getPlatform() {
        return platform;
    }

    public Action setPlatform(String platform) {
        this.platform = platform;
        return this;
    }

}
