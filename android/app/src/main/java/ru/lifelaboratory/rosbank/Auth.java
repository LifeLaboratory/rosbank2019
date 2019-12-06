package ru.lifelaboratory.rosbank;

public class Auth {

    private String login;
    private String password;

    public String getLogin() {
        return login;
    }

    public Auth setLogin(String login) {
        this.login = login;
        return this;
    }

    public String getPassword() {
        return password;
    }

    public Auth setPassword(String password) {
        this.password = password;
        return this;
    }
}
