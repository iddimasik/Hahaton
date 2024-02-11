package ru.seals.spring.App.models;

import javax.persistence.*;

@Entity
@Table(name = "cleaning_day")
public class CleaningDay {
    @Id
    @Column(name = "id")
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int id;

    @Column(name = "clean_title")
    private String cleanTitle;

    @Column(name = "clean_text")
    private String cleanText;

    @Column(name = "count_people")
    private int countPeople;

    @ManyToOne
    @JoinColumn(name = "pollution_place_id", referencedColumnName = "id")
    private TrashPlace trashPlace;

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getCleanTitle() {
        return cleanTitle;
    }

    public void setCleanTitle(String cleanTitle) {
        this.cleanTitle = cleanTitle;
    }

    public String getCleanText() {
        return cleanText;
    }

    public void setCleanText(String cleanText) {
        this.cleanText = cleanText;
    }

    public int getCountPeople() {
        return countPeople;
    }

    public void setCountPeople(int countPeople) {
        this.countPeople = countPeople;
    }

    public TrashPlace getTrashPlace() {
        return trashPlace;
    }

    public void setTrashPlace(TrashPlace trashPlace) {
        this.trashPlace = trashPlace;
    }
}
