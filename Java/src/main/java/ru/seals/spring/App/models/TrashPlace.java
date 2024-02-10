package ru.seals.spring.App.models;

import ru.seals.spring.App.util.UserStatus;
import javax.persistence.*;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.Date;

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

    @Column(name = "region_id")
    private int regionId;

    @Column(name = "user_id")
    private int userId;

    @Column(name = "creation_date")
    private LocalDateTime date;

    @Column(name = "coordinates_xy")
    private String coordinates;

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

    public int getRegionId() {
        return regionId;
    }
    public void setRegionId(int regionId) {
        this.regionId = regionId;
    }

    public int getUserId() {
        return userId;
    }
    public void setUserId(int userId) {
        this.userId = userId;
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
}
