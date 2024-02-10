package ru.seals.spring.App.models;

import ru.seals.spring.App.repositories.ImageRep;
import ru.seals.spring.App.util.UserStatus;
import javax.persistence.*;
import java.util.Date;

@Entity
@Table(name = "Images")
public class Images {

    @Id
    @Column(name = "id")
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int id;

    @Column(name = "image_data")
    private byte imageData;

    @Column(name = "pollution_place_id")
    private int placeId;

    public int getId() {
        return id;
    }
    public void setId(int id) {
        this.id = id;
    }

    public byte getImageData() {
        return imageData;
    }

    public void setImageData(byte imageData) {
        this.imageData = imageData;
    }

    public int getPlaceId() {
        return placeId;
    }
    public void setPlaceId(int placeId) {
        this.placeId = placeId;
    }
}
