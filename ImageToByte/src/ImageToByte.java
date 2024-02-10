import java.awt.image.BufferedImage;
import java.io.*;
import javax.imageio.ImageIO;
import java.util.Base64;

public class ImageToByte {
    public static void main(String[] args) throws IOException {
        String imagePath = "example.jpg";
        String textFilePath = "photo.txt";

        //convertImageToBytesAndSave(imagePath, textFilePath);
        convertBytesFromFileToImage(textFilePath, "resultImage.jpg");
    }

    static void convertImageToBytesAndSave(String imagePath, String textFilePath) {
        try (ByteArrayOutputStream baos = new ByteArrayOutputStream()) {
            BufferedImage image = ImageIO.read(new File(imagePath));
            ImageIO.write(image, "jpg", baos);
            byte[] imageBytes = baos.toByteArray();

            String base64String = Base64.getEncoder().encodeToString(imageBytes);

            try (FileWriter writer = new FileWriter(textFilePath)) {
                writer.write(base64String);
                System.out.println("Данные изображения успешно сохранены в файле: " + textFilePath);
            } catch (IOException e) {
                System.err.println("Ошибка при записи данных изображения в файл: " + e.getMessage());
            }
        } catch (IOException e) {
            System.err.println("Ошибка при конвертации изображения в байты: " + e.getMessage());
        }
    }

    static void convertBytesFromFileToImage(String textFilePath, String outputImagePath) {
        try (BufferedReader reader = new BufferedReader(new FileReader(textFilePath))) {
            StringBuilder stringBuilder = new StringBuilder();
            String line;
            while ((line = reader.readLine()) != null) {
                stringBuilder.append(line);
            }
            String base64String = stringBuilder.toString();
            byte[] decodedBytes = Base64.getDecoder().decode(base64String);

            ByteArrayInputStream bais = new ByteArrayInputStream(decodedBytes);
            BufferedImage resultImage = ImageIO.read(bais);
            ImageIO.write(resultImage, "jpg", new File(outputImagePath));
            System.out.println("Изображение успешно восстановлено из файла: " + outputImagePath);
        } catch (IOException e) {
            System.err.println("Ошибка при чтении данных из файла или записи изображения: " + e.getMessage());
        }
    }
}