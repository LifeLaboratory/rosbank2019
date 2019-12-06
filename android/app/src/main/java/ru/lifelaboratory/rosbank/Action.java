package ru.lifelaboratory.rosbank;

public class Action {

    private Integer idUser;
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
