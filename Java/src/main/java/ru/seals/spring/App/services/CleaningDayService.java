package ru.seals.spring.App.services;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import ru.seals.spring.App.models.CleaningDay;
import ru.seals.spring.App.repositories.CleaningDayRep;

import java.util.List;

@Service
public class CleaningDayService {

    private final CleaningDayRep cleaningDayRep;

    @Autowired
    public CleaningDayService(CleaningDayRep cleaningDayRep) {
        this.cleaningDayRep = cleaningDayRep;
    }

    public List<CleaningDay> findAll() {
        return cleaningDayRep.findAll();
    }

    public CleaningDay findOne(int id) {
        return cleaningDayRep.findById(id).orElse(null);
    }

    public void save(CleaningDay typeCourse) {
        cleaningDayRep.save(typeCourse);
    }


    public void update(int id, CleaningDay updatedTypeCourse) {
        updatedTypeCourse.setId(id);
        cleaningDayRep.save(updatedTypeCourse);
    }

    public void delete(int id) {
        cleaningDayRep.deleteById(id);
    }
}
