package ru.lifelaboratory.rosbank;

import com.google.gson.annotations.SerializedName;

public class User {

    private String login;
    private String password;
    @SerializedName("id_user")
    private Integer idUser;
    private String message;

    public String getLogin() {
        return login;
    }

    public User setLogin(String login) {
        this.login = login;
        return this;
    }

    public String getPassword() {
        return password;
    }

    public User setPassword(String password) {
        this.password = password;
        return this;
    }

    public Integer getIdUser() {
        return idUser;
    }

    public User setIdUser(Integer idUser) {
        this.idUser = idUser;
        return this;
    }

    public String getMessage() {
        return message;
    }

    public User setMessage(String message) {
        this.message = message;
        return this;
    }
}
