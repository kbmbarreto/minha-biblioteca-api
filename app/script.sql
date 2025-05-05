CREATE DATABASE IF NOT EXISTS minha_biblioteca;
USE minha_biblioteca;

CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    year INT NOT NULL,
    publishing_company VARCHAR(255) NOT NULL,
    is_readed BOOLEAN DEFAULT FALSE,
    is_digital BOOLEAN DEFAULT FALSE,
    is_deleted BOOLEAN DEFAULT FALSE,
    cover VARCHAR(255),
    updated_date DATETIME DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO books (title, author, year, publishing_company, is_readed, is_digital, is_deleted, cover, updated_date) VALUES
('O Senhor dos Anéis: A Sociedade do Anel', 'J.R.R. Tolkien', 1954, 'HarperCollins', TRUE, FALSE, FALSE, 'https://m.media-amazon.com/images/I/91+0Bbd8y5L.jpg', NOW()),
('1984', 'George Orwell', 1949, 'Companhia das Letras', TRUE, TRUE, FALSE, 'https://m.media-amazon.com/images/I/71kxa1-0mfL.jpg', NOW()),
('Dom Casmurro', 'Machado de Assis', 1899, 'Editora Ática', FALSE, FALSE, FALSE, 'https://m.media-amazon.com/images/I/71qJkpu3KjL.jpg', NOW()),
('A Revolução dos Bichos', 'George Orwell', 1945, 'Companhia das Letras', TRUE, TRUE, FALSE, 'https://m.media-amazon.com/images/I/81zoN1rI85L.jpg', NOW()),
('Harry Potter e a Pedra Filosofal', 'J.K. Rowling', 1997, 'Rocco', TRUE, FALSE, FALSE, 'https://m.media-amazon.com/images/I/81YOuOGFCJL.jpg', NOW()),
('O Hobbit', 'J.R.R. Tolkien', 1937, 'HarperCollins', TRUE, FALSE, FALSE, 'https://m.media-amazon.com/images/I/91b0C2YNSrL.jpg', NOW());
