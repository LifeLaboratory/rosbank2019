package ru.lifelaboratory.rosbank;

import com.google.gson.annotations.SerializedName;

import java.util.List;

public class Stories {

    @SerializedName("id_stories")
    private Integer id;
    private List<String> image;

    public Integer getId() {
        return id;
    }

    public Stories setId(Integer id) {
        this.id = id;
        return this;
    }

    public List<String> getImage() {
        return image;
    }

    public Stories setImage(List<String> image) {
        this.image = image;
        return this;
    }
}
