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
    private String imageData;

    @ManyToOne
    @JoinColumn(name = "pollution_place_id", referencedColumnName = "id")
    private TrashPlace trashPlace;

    public int getId() {
        return id;
    }
    public void setId(int id) {
        this.id = id;
    }

    public String getImageData() {
        return imageData;
    }

    public void setImageData(String imageData) {
        this.imageData = imageData;
    }

    public TrashPlace getTrashPlace() {
        return trashPlace;
    }

    public void setTrashPlace(TrashPlace trashPlace) {
        this.trashPlace = trashPlace;
    }
}
