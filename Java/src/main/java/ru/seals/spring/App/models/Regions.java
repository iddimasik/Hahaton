package ru.seals.spring.App.models;

import ru.seals.spring.App.util.UserStatus;
import javax.persistence.*;

@Entity
@Table(name = "Regions")
public class Regions {

    @Id
    @Column(name = "id")
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int id;

    @Column(name = "region_name")
    private String regionName;

    public int getId() {
        return id;
    }
    public void setId(int id) {
        this.id = id;
    }

    public String getRegionName() {
        return regionName;
    }
    public void setRegionName(String regionName) {
        this.regionName = regionName;
    }
}
