package ru.seals.spring.App.services;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.stereotype.Service;
import ru.seals.spring.App.models.Regions;
import ru.seals.spring.App.models.TrashPlace;
import ru.seals.spring.App.repositories.TrashPlaceRep;

import java.util.List;

@Service
public class PlaceProblemService {
    private final TrashPlaceRep trashPlaceRep;

    @Autowired
    public PlaceProblemService(TrashPlaceRep trashPlaceRep) {
        this.trashPlaceRep = trashPlaceRep;
    }

    public List<TrashPlace> findAll() {
        return trashPlaceRep.findAll();
    }

    public TrashPlace findOne(int id) {
        return trashPlaceRep.findById(id).orElse(null);
    }

    public void save(TrashPlace typeCourse) {
        trashPlaceRep.save(typeCourse);
    }

    public void update(int id, TrashPlace updatedTypeCourse) {
        updatedTypeCourse.setId(id);
        trashPlaceRep.save(updatedTypeCourse);
    }


    public void delete(int id) {
        trashPlaceRep.deleteById(id);
    }
}
