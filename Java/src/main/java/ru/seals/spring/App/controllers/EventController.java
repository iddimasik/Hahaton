package ru.seals.spring.App.controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.RequestMapping;
import ru.seals.spring.App.models.CleaningDay;
import ru.seals.spring.App.services.PlaceProblemService;

@Controller
@RequestMapping("/event")
public class EventController {

    private final PlaceProblemService placeProblemService;

    @Autowired
    public EventController(PlaceProblemService placeProblemService) {
        this.placeProblemService = placeProblemService;
    }

    @GetMapping("/addEvent")
    public String addEvent(@ModelAttribute("event") CleaningDay cleaningDay, Model model) {
        model.addAttribute("problem",placeProblemService.findAll());
        return "event/addEvent";
    }
}
