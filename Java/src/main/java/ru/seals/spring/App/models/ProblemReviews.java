package ru.seals.spring.App.models;

import ru.seals.spring.App.util.UserStatus;
import javax.persistence.*;
import java.util.Date;

@Entity
@Table(name = "problem_reviews")
public class ProblemReviews {

            @Id
            @Column(name = "id")
            @GeneratedValue(strategy = GenerationType.IDENTITY)
            private int id;

            @Column(name = "review_author")
            private String author;

            @Column(name = "review_text")
            private String revText;

            @Column(name = "creation_date")
            private Date revDate;

            @Column(name = "publication_status")
            private String publicationStatus;

            @Column(name = "pollution_place_id")
            private int placeId;

            @Column(name = "user_id")
            private int userId;

            public int getId() {
                return id;
            }

            public void setId(int id) {
                this.id = id;
            }

            public String getAuthor() {
                return author;
            }

            public void setAuthor(String author) {
                this.author = author;
            }

            public String getRevText() {
                return revText;
            }

            public void setRevText(String revText) {
                this.revText = revText;
            }

            public Date getRevDate() {
                return revDate;
            }

            public void setRevDate(Date revDate) {
                this.revDate = revDate;
            }

            public String getPublicationStatus() {
                return publicationStatus;
            }

            public void setPublicationStatus(String publicationStatus) {
                this.publicationStatus = publicationStatus;
            }

            public int getPlaceId() {
                return placeId;
            }

            public void setPlaceId(int placeId) {
                this.placeId = placeId;
            }

            public int getUserId() {
                return userId;
            }

            public void setUserId(int userId) {
                this.userId = userId;
            }
}
