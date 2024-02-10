package ru.seals.spring.App.util;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import ru.seals.spring.App.models.Images;
import ru.seals.spring.App.models.TrashPlace;
import ru.seals.spring.App.services.ImageService;

import java.awt.image.BufferedImage;
import java.io.*;
import javax.imageio.ImageIO;
import java.util.Base64;

@Component
public class ImageToByte {

    private final ImageService imageService;

    @Autowired
    public ImageToByte(ImageService imageService) {
        this.imageService = imageService;
    }


    public void convertImageToBytesAndSave(String imagePath, TrashPlace trashPlace) {
        try (ByteArrayOutputStream baos = new ByteArrayOutputStream()) {
            BufferedImage image = ImageIO.read(new File(imagePath));
            ImageIO.write(image, "jpg", baos);
            byte[] imageBytes = baos.toByteArray();
            System.out.println(imagePath);
            String base64String = Base64.getEncoder().encodeToString(imageBytes);
            Images images = new Images();
            images.setImageData(base64String);
            images.setTrashPlace(trashPlace);
            imageService.save(images);
            System.out.println("Сохранено");
        } catch (IOException e) {
            System.err.println("Ошибка при конвертации изображения в байты: " + e.getMessage());
        }
    }

    public String convertBytesFromFileToImage(int id) throws IOException {
            String outputImagePath = "C:\\Users\\Antares\\Desktop\\Seahack\\Hahaton\\Java\\src\\main\\resources\\static\\img\\resultImage" + id + ".jpg";
            String base64String = imageService.findByPollutionPlace(id).getImageData();
            byte[] decodedBytes = Base64.getDecoder().decode(base64String);

            ByteArrayInputStream bais = new ByteArrayInputStream(decodedBytes);
            BufferedImage resultImage = ImageIO.read(bais);
            ImageIO.write(resultImage, "jpg", new File(outputImagePath));
             System.out.println(outputImagePath);
            return outputImagePath;
    }
}
