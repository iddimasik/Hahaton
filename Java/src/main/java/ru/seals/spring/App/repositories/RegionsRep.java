package ru.seals.spring.App.repositories;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import ru.seals.spring.App.models.Regions;

@Repository
public interface RegionsRep extends JpaRepository<Regions,Integer> {

}
