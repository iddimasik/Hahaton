package ru.seals.spring.App.controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;
import ru.seals.spring.App.models.Person;
import ru.seals.spring.App.models.Regions;
import ru.seals.spring.App.models.TrashPlace;
import ru.seals.spring.App.services.PersonDetailsService;
import ru.seals.spring.App.services.PlaceProblemService;
import ru.seals.spring.App.services.RegionService;

import javax.validation.Valid;
import java.time.LocalDate;
import java.time.LocalDateTime;

@Controller
@RequestMapping("/problem")
public class PlaceProblemController {

    private final PersonDetailsService personDetailsService;
    private final RegionService regionService;
    private final PlaceProblemService placeProblemService;

    @Autowired
    public PlaceProblemController(PersonDetailsService personDetailsService, RegionService regionService, PlaceProblemService placeProblemService) {
        this.personDetailsService = personDetailsService;
        this.regionService = regionService;
        this.placeProblemService = placeProblemService;
    }

    @GetMapping("/add")
    public String addProblem(@ModelAttribute("problem") TrashPlace trashPlace, Model model) {
        model.addAttribute("regions",regionService.findAll());
        return "problems/addProblem";
    }

    @PostMapping("/add")
    public String doProblem(@ModelAttribute("problem") @Valid TrashPlace trashPlace, @RequestParam("latitude") double latitude, @RequestParam("longitude") double longitude, @RequestParam("region")int region) {
        Authentication authentication = SecurityContextHolder.getContext().getAuthentication();
        Person person = personDetailsService.loadPersonByLogin(authentication.getName());
        trashPlace.setRegionId(region);
        trashPlace.setUserId(person.getId());
        trashPlace.setDate(LocalDateTime.now());
        trashPlace.setCoordinates(latitude + "," + longitude);
        trashPlace.setProblemStatus("На рассмотрении");
        placeProblemService.save(trashPlace);
        return "redirect:/hello";
    }

}
