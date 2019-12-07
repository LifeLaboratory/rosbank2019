package ru.lifelaboratory.rosbank;

import com.google.gson.annotations.SerializedName;

import java.util.List;

public class Notification {

    @SerializedName("id_notification")
    private Integer id;
    private String name;
    private String url;
    private List<String> image;
    private List<String> description;
    private Integer type;

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

    public List<String> getImage() {
        return image;
    }

    public Notification setImage(List<String> image) {
        this.image = image;
        return this;
    }

    public List<String> getDescription() {
        return description;
    }

    public Notification setDescription(List<String> description) {
        this.description = description;
        return this;
    }

    public Integer getType() {
        return type;
    }

    public Notification setType(Integer type) {
        this.type = type;
        return this;
    }
}
