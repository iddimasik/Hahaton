package ru.seals.spring.App.services;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.stereotype.Service;
import ru.seals.spring.App.models.Regions;
import ru.seals.spring.App.repositories.RegionsRep;

import java.util.List;

@Service
public class RegionService {

    private final RegionsRep regionsRep;

    @Autowired
    public RegionService(RegionsRep regionsRep) {
        this.regionsRep = regionsRep;
    }

    public List<Regions> findAll() {
        return regionsRep.findAll();
    }

    public Regions findOne(int id) {
        return regionsRep.findById(id).orElse(null);
    }

    public void save(Regions typeCourse) {
        regionsRep.save(typeCourse);
    }


    public void update(int id, Regions updatedTypeCourse) {
        updatedTypeCourse.setId(id);
        regionsRep.save(updatedTypeCourse);
    }

    public void delete(int id) {
        regionsRep.deleteById(id);
    }
}
