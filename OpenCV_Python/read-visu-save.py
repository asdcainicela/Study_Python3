import cv2

imagen = cv2.imread('OpenCv_Python/img/img_zero.jpg', 1) # buscar imagen
cv2.imshow("Prueba de imagen ", imagen) # mostrar imagen
cv2.imwrite('OpenCv_Python/img/copy_img_zero.jpg', imagen) # save imagen
cv2.waitKey(0)  # tiempo de espera
cv2.destroyAllWindows() # cerrar window
