package ru.lifelaboratory.rosbank;

import com.google.gson.annotations.SerializedName;

import java.util.List;

public class Notification {

    @SerializedName("id_notification")
    private Integer id;
    private String name;
    private String url;

    public Integer getId() {
        return id;
    }

    public Notification setId(Integer id) {
        this.id = id;
        return this;
    }

    public String getName() {
        return name;
    }

    public Notification setName(String name) {
        this.name = name;
        return this;
    }

    public String getUrl() {
        return url;
    }

    public Notification setUrl(String url) {
        this.url = url;
        return this;
    }
}
