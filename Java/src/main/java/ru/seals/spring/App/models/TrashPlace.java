package ru.seals.spring.App.models;

import ru.seals.spring.App.util.UserStatus;
import javax.persistence.*;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.Date;
import java.util.List;

@Entity
@Table(name = "Pollution_Places")
public class TrashPlace {

    @Id
    @Column(name = "id")
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int id;

    @Column(name = "problem_title")
    private String title;

    @Column(name = "problem_text")
    private String text;

    @Column(name = "problem_status")
    private String problemStatus;

    @ManyToOne
    @JoinColumn(name = "region_id", referencedColumnName = "id")
    private Regions region;

    @ManyToOne
    @JoinColumn(name = "user_id", referencedColumnName = "id")
    private Person person;

    @Column(name = "creation_date")
    private LocalDateTime date;

    @Column(name = "coordinates_xy")
    private String coordinates;

    @OneToMany(mappedBy = "trashPlace")
    private List<Images> trashPlaces;

    public int getId() {
        return id;
    }
    public void setId(int id) {
        this.id = id;
    }

    public String getTitle() {
        return title;
    }
    public void setTitle(String title) {
        this.title = title;
    }

    public String getText() {
        return text;
    }
    public void setText(String text) {
        this.text = text;
    }

    public String getProblemStatus() {
        return problemStatus;
    }
    public void setProblemStatus(String problemStatus) {
        this.problemStatus = problemStatus;
    }

    public Regions getRegion() {
        return region;
    }

    public void setRegion(Regions region) {
        this.region = region;
    }

    public Person getPerson() {
        return person;
    }

    public void setPerson(Person person) {
        this.person = person;
    }

    public LocalDateTime getDate() {
        return date;
    }
    public void setDate(LocalDateTime date) {
        this.date = date;
    }

    public String getCoordinates() {
        return coordinates;
    }
    public void setCoordinates(String coordinates) {
        this.coordinates = coordinates;
    }

    public List<Images> getTrashPlaces() {
        return trashPlaces;
    }

    public void setTrashPlaces(List<Images> trashPlaces) {
        this.trashPlaces = trashPlaces;
    }

    @Override
    public String toString() {
        return coordinates;
    }
}
