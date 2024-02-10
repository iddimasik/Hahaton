package ru.seals.spring.App.controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import ru.seals.spring.App.security.PersonDetails;
import ru.seals.spring.App.services.AdminService;
import ru.seals.spring.App.services.PlaceProblemService;

@Controller
public class HelloController {

    private final AdminService adminService;
    private final PlaceProblemService placeProblemService;

    @Autowired
    public HelloController(AdminService adminService, PlaceProblemService placeProblemService) {
        this.adminService = adminService;
        this.placeProblemService = placeProblemService;
    }

    @GetMapping("/hello")
    public String sayHello(Model model) {
        model.addAttribute("problems",placeProblemService.findAll());
        return "hello";
    }

    @GetMapping("/showUserInfo")
    public String showUserInfo() {
        Authentication authentication = SecurityContextHolder.getContext().getAuthentication();
        PersonDetails personDetails = (PersonDetails) authentication.getPrincipal();
        System.out.println(personDetails.getPerson());

        return "hello";
    }

    @GetMapping("/admin")
    public String adminPage() {
        adminService.doAdminStuff();
        return "admin";
    }
}
