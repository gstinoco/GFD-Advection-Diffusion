# mGFD-Advection-Diffusion
Data and methods for numerically solve Advection-Diffusion Equation using a meshless Generalized Finite Differences Scheme.

All the codes are distributed under MIT License on [GitHub](https://github.com/gstinoco/GFD-Advection-Diffusion) and are free to use, modify, and distribute giving the proper copyright notice.

## Description :memo:
This repository proposes a way to achieve an approximation to Advection-Diffusion Equation in two dimensions for highly irregular regions.

For this, the proposed method uses a Generalized Finite Differences Method for the numerical solution on unstructured clouds of points.

Examples of solving various problems in an irregular region can be found below.

| Titicaca Lake Cloud of Points                                                                        | Titicaca Lake Cloud of Points with Holes                                                             |
| :--------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------:|
| <img src="Data/Clouds/TIT.png">                                                                      | <img src="Data/Holes/TIT.png">                                                                       |
|                                                                                                      |                                                                                                      |
| Example 1                                                                                                                                                                                                  ||
| <video src="https://github.com/user-attachments/assets/bd93859d-eeac-4c9e-b36e-d68aa0b9c413">        | <video src="https://github.com/user-attachments/assets/e2d2f527-ac39-44ac-9faf-6975c28c8fb6">        |
| $\mid\mid e\mid\mid = 5.2118943754735635e-08$                                                        | $\mid\mid e\mid\mid = 4.863648258963009e-08$                                                         |
|                                                                                                      |                                                                                                      |
| Example 2                                                                                                                                                                                                  ||
| <video src="https://github.com/user-attachments/assets/3a296664-5b6b-4f91-99d3-dae1359fd80c">        | <video src="https://github.com/user-attachments/assets/897b22b5-78af-41e0-9bbd-ebe9e4af7892">        |
| $\mid\mid e\mid\mid = 1.0322904171601065e-04$                                                        | $\mid\mid e\mid\mid = 1.0828264528519587e-04$                                                        |
|                                                                                                      |                                                                                                      |
| Example 3                                                                                                                                                                                                  ||
| <video src="https://github.com/user-attachments/assets/13e992d8-6884-4428-95f2-83f6639c1555">        | <video src="https://github.com/user-attachments/assets/94d2a0cc-3d48-4c50-9494-568be0b2faf5">        |
| $\mid\mid e\mid\mid = 1.0731208462156676e-04$                                                        | $\mid\mid e\mid\mid = 1.1097288200407238e-04$                                                        |
|                                                                                                      |                                                                                                      |
| Example 4                                                                                                                                                                                                  ||
| <video src="https://github.com/user-attachments/assets/6e1bc418-d28a-497f-a391-b8a5efd77cd6">        | <video src="https://github.com/user-attachments/assets/bb4dfc77-afb8-48d8-9da9-acf5bacc38a6">        |
| $\mid\mid e\mid\mid = 1.9083623596292698e-03$                                                        | $\mid\mid e\mid\mid = 2.229806198931734e-03$                                                         |
|                                                                                                      |                                                                                                      |
| Example 5                                                                                                                                                                                                  ||
| <video src="https://github.com/user-attachments/assets/bd434f9d-3bb0-4372-b1e2-e4a5acfc4c6c">        | <video src="https://github.com/user-attachments/assets/7a59a4c3-5916-49a6-951d-74fc8106512c">        |
| $\mid\mid e\mid\mid = 9.589504723286449e-04$                                                         | $\mid\mid e\mid\mid = 1.485761180356545e-03$                                                         |
|                                                                                                      |                                                                                                      |
| Example 6                                                                                                                                                                                                  ||
| <video src="https://github.com/user-attachments/assets/548b4b31-f1aa-480b-b755-5ca5d59da859">        | <video src="https://github.com/user-attachments/assets/019796dd-53c3-47f5-a21f-76a29d5630ec">        |
| $\mid\mid e\mid\mid = 4.155055732537449e-05$                                                         | $\mid\mid e\mid\mid = 4.649037082216217e-05$                                                         |
|                                                                                                      |                                                                                                      |
| Example 7                                                                                                                                                                                                  ||
| <video src="https://github.com/user-attachments/assets/e3be65a4-1f34-43d3-9365-e84367119a9c">        | <video src="https://github.com/user-attachments/assets/e9e03cb6-1944-4fd4-a5c5-c88a4a8a0b00">        |
| $\mid\mid e\mid\mid = 1.0882583340529215e-03$                                                        | $\mid\mid e\mid\mid = 1.1889349763568261e-03$                                                        |


## Data :open_file_folder:
All the data were taken from Author's [Cloud-Generation Github Repository](https://github.com/gstinoco/Cloud-Generation). The data is free for anyone to use to compare the results using different methods with the same dataset.

The following regions were considered for this repository:
- **BAN**: Banderas bay in Mexico.
- **BLU**: Blue Lagoon in Iceland.
- **CUA**: Unitary square.
- **CUI**: Cuitzeo Lake in Mexico.
- **ENG**: United Kingdom Island.
- **GIB**: Strait of Gibraltar.
- **HAB**: Havana bay.
- **MIC**: Michoacan State in Mexico.
- **PAT**: Patzcuaro Lake in Mexico.
- **TIT**: Titicaca Lake in South America.
- **TOB**: Toba Lake in Indonesia.
- **UCH**: Uchinskoye Reservoir in Russia.
- **VAL**: Valencia Lake in Spain.
- **ZIR**: Zirahuen Lake in Mexico

## How to :microscope:
The codes are self explained and completely documented. Examples on how to perform approximations can be found on the files that approximate the following conditions:
- **Example_1.py**: $$f(x, y, v, a, b, t) = \left(\frac{1}{4t + 1}\right)\exp\left(-\frac{(x - at - 0.5)^2}{v(4t + 1)} - \frac{(y - bt - 0.5)^2}{v(4t + 1)}\right)$$

- **Example_2.py**: $$f(x, y, v, a, b, t) = \frac{1}{4\pi v t + 1} \exp\left(-\frac{(x - a t)^2 + (y - b t)^2}{4v t + 1}\right)$$

- **Example_3.py**: $$f(x, y, v, a, b, t) = \sin(\pi (x - a t)) \cdot \sin(\pi (y - b t)) \cdot \exp(-v t)$$

- **Example_4.py**: $$f(x, y, v, a, b, t) =  \text{ for } 0.2 < x - a t < 0.8 \text{ and } 0.2 < y - b$$

- **Example_5.py**: $$f(x, y, v, a, b, t) = \exp\left(-\frac{(x - a t)^2 + (y - b t)^2}{4v t + 1}\right) \cdot \mathbf{1}(x^2 + y^2 \leq 0.25)$$

- **Example_6.py**: $$f(x, y, v, a, b, t) = \exp\left(-100 \cdot ((x - 0.5 - a t)^2 + (y - 0.5 - b t)^2)\right) \cdot \exp(-v t)$$

- **Example_7.py**: $$f(x, y, v, a, b, t) = \mathbf{H}(0.5 - (x - a t)) \cdot \mathbf{H}(0.5 - (y - b t))$$

These examples can be easily modified to perform approximations with different conditions and coefficients.

## Researchers :scientist:
All the codes presented were developed by:
    
  - **Dr. Gerardo Tinoco Guerrero**<br>
    Universidad Michoacana de San Nicolás de Hidalgo<br>
    Aula CIMNE-Morelia<br>
    gerardo.tinoco@umich.mx<br>
    https://orcid.org/0000-0003-3119-770X

  - **Dr. Francisco Javier Domínguez Mota**<br>
    Universidad Michoacana de San Nicolás de Hidalgo<br>
    Aula CIMNE-Morelia<br>
    francisco.mota@umich.mx<br>
    https://orcid.org/0000-0001-6837-172X

  - **Dr. José Alberto Guzmán Torres**<br>
    Universidad Michoacana de San Nicolás de Hidalgo<br>
    Aula CIMNE-Morelia<br>
    jose.alberto.guzman@umich.mx<br>
    https://orcid.org/0000-0002-9309-9390

  - **Dr. José Gerardo Tinoco Ruiz**<br>
    Universidad Michoacana de San Nicolás de Hidalgo<br>
    jose.gerardo.tinoco@umich.mx<br>
    https://orcid.org/0000-0002-0866-4798

## Students :man_student: :woman_student:
  - **Heriberto Arias Rojas**<br>
    Universidad Michoacana de San Nicolás de Hidalgo<br>
    heriberto.arias@umich.mx<br>
    https://orcid.org/0000-0002-7641-8310

  - **Gabriela Pedraza Jiménez**<br>
    Universidad Michoacana de San Nicolás de Hidalgo<br>
    2220157h@umich.mx<br>
    https://orcid.org/0009-0002-8118-0260
  
  - **Miguel Ángel Rodríguez Velázquez**<br>
    Universidad Michoacana de San Nicolás de Hidalgo<br>
    miguel.rodriguez@umich.mx<br>
    https://orcid.org/0009-0009-7245-1517
  
  - **Ricardo Román Gutiérrez**<br>
    Universidad Michoacana de San Nicolás de Hidalgo<br>
    ricardo.roman@umich.mx<br>
    https://orcid.org/0000-0001-8521-9391

<!--
  - **Nancy Saray Saucedo León**<br>
    Universidad Michoacana de San Nicolás de Hidalgo<br>
    1153558a@umich.mx<br>
-->
## Funding :dollar:
With the financing of:

  - National Council of Humanities, Sciences and Technologies, CONAHCyT (Consejo Nacional de Humanidades, Ciencias y Tecnologías, CONAHCyT), México.
  
  - Coordination of Scientific Research, CIC-UMSNH (Coordinación de la Investigación Científica de la Universidad Michoacana de San Nicolás de Hidalgo, CIC-UMSNH), México.
  
  - Aula CIMNE-Morelia, México.
