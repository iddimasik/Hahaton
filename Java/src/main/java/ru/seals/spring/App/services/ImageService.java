package ru.seals.spring.App.services;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import ru.seals.spring.App.models.Images;
import ru.seals.spring.App.models.Regions;
import ru.seals.spring.App.repositories.ImageRep;

import java.util.List;

@Service
public class ImageService {

    private final ImageRep imageRep;

    @Autowired
    public ImageService(ImageRep imageRep) {
        this.imageRep = imageRep;
    }

    public List<Images> findAll() {
        return imageRep.findAll();
    }

    public Images findOne(int id) {
        return imageRep.findById(id).orElse(null);
    }

    public Images findByPollutionPlace(int id) {
        return imageRep.findByPollutionPlaceId(id).orElse(null);
    }

    public void save(Images typeCourse) {
        imageRep.save(typeCourse);
    }


    public void update(int id, Images updatedTypeCourse) {
        updatedTypeCourse.setId(id);
        imageRep.save(updatedTypeCourse);
    }

    public void delete(int id) {
        imageRep.deleteById(id);
    }
}
