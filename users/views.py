from pyexpat.errors import messages
from django.shortcuts import render

from users.forms import UserRegistrationForm
from users.models import UserRegistrationModel

# Create your views here.

def base(request):
    return render(request,'base.html')

from django.shortcuts import render
from django.contrib import messages
from .forms import UserRegistrationForm

def base(request):
    return render(request, 'base.html')  # Or 'users/home.html' if using a homepage template

from django.shortcuts import render
from django.contrib import messages
from .forms import UserRegistrationForm

def base(request):
    return render(request, 'base.html')

def index(request):
    return render(request,'index.html')

def UserRegisterActions(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have been successfully registered!')
            return render(request, 'UserRegistration.html', {'form': UserRegistrationForm()})
        else:
            if form.errors.get('emailid') or form.errors.get('mobileno'):
                messages.error(request, 'Email or Mobile Number already exists.')
            else:
                messages.error(request, 'Please correct the errors below.')
    else:
        form = UserRegistrationForm()
    return render(request, 'UserRegistration.html', {'form': form})

def UserLoginCheck(request):
    if request.method == "POST":
        loginid = request.POST.get('loginid')  # Corrected to 'loginid'
        pswd = request.POST.get('pswd')        # Corrected to 'pswd'
        print("Login ID = ", loginid, ' Password = ', pswd)
        try:
            check = UserRegistrationModel.objects.get(
                loginid=loginid, password=pswd)
            status = check.status
            print('Status is = ', status)
            if status == "activated":
                request.session['id'] = check.id
                request.session['loggeduser'] = check.name
                request.session['loginid'] = loginid
                request.session['email'] = check.email
                print("User id At", check.id, status)
                return render(request, 'users/UserHome.html', {})
            else:
                messages.success(request, 'Your Account is not activated')
                return render(request, 'UserLogin.html')
        except Exception as e:
            print('Exception is ', str(e))
            pass
        messages.success(request, 'Invalid Login id and password')
    return render(request, 'UserLogin.html', {})


def UserHome(request):
    return render(request, 'users/UserHome.html', {})



###########################DL CODE####################################### 

import os
import sys
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend for server-side rendering
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from django.shortcuts import render
from django.http import HttpResponse
import datetime

def training(request):
    try:
        base_path = r'C:\Fruit_Identification_Using_Convolutional_Neural_Network\media\Fruit-Images-Dataset-master\Fruit-Images-Dataset-master'
        train_dir = os.path.join(base_path, 'Training')
        test_dir = os.path.join(base_path, 'Test')

        if not os.path.exists(train_dir) or not os.path.exists(test_dir):
            return HttpResponse("Error: Training or Test directories not found. Please check your dataset path.")

        NUM_CLASSES = len([name for name in os.listdir(train_dir) if os.path.isdir(os.path.join(train_dir, name))])

        IMG_SIZE = 100
        BATCH_SIZE = 32

        train_datagen = ImageDataGenerator(
            rescale=1./255,
            rotation_range=20,
            width_shift_range=0.2,
            height_shift_range=0.2,
            shear_range=0.2,
            zoom_range=0.2,
            horizontal_flip=True,
            fill_mode='nearest',
            validation_split=0.2
        )

        test_datagen = ImageDataGenerator(rescale=1./255)

        train_generator = train_datagen.flow_from_directory(
            train_dir,
            target_size=(IMG_SIZE, IMG_SIZE),
            batch_size=BATCH_SIZE,
            class_mode='categorical',
            subset='training',
            shuffle=True
        )

        val_generator = train_datagen.flow_from_directory(
            train_dir,
            target_size=(IMG_SIZE, IMG_SIZE),
            batch_size=BATCH_SIZE,
            class_mode='categorical',
            subset='validation',
            shuffle=True
        )

        test_generator = test_datagen.flow_from_directory(
            test_dir,
            target_size=(IMG_SIZE, IMG_SIZE),
            batch_size=BATCH_SIZE,
            class_mode='categorical',
            shuffle=False
        )

        model = models.Sequential([
            layers.Conv2D(32, (3, 3), activation='relu', input_shape=(IMG_SIZE, IMG_SIZE, 3)),
            layers.MaxPooling2D((2, 2)),
            layers.Conv2D(64, (3, 3), activation='relu'),
            layers.MaxPooling2D((2, 2)),
            layers.Conv2D(128, (3, 3), activation='relu'),
            layers.MaxPooling2D((2, 2)),
            layers.Flatten(),
            layers.Dense(512, activation='relu'),
            layers.Dropout(0.5),
            layers.Dense(NUM_CLASSES, activation='softmax')
        ])

        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

        history = model.fit(
            train_generator,
            epochs=10,
            validation_data=val_generator,
            steps_per_epoch=500,
            validation_steps=val_generator.samples // BATCH_SIZE
        )

        test_loss, test_accuracy = model.evaluate(test_generator)

        # Save model
        model_path = os.path.join(base_path, 'fruit_cnn_model.h5')
        model.save(model_path)

        # Save accuracy plot to static or media
        timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        plot_path = os.path.join(base_path, f'training_plot_{timestamp}.png')

        plt.figure()
        plt.plot(history.history['accuracy'], label='Training Accuracy')
        plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
        plt.title('Model Accuracy Over Epochs')
        plt.xlabel('Epoch')
        plt.ylabel('Accuracy')
        plt.legend()
        plt.savefig(plot_path)
        plt.close()

        return render(request, 'users/training.html', {
            'test_accuracy': f"{test_accuracy*100:.2f}%",
            'plot_path': f"/media/training_plot_{timestamp}.png"
        })

    except Exception as e:
        return HttpResponse(f"Training failed with error: {str(e)}")
    

import os
import numpy as np
import tensorflow as tf
from django.shortcuts import render
from django.core.files.storage import default_storage
from django.conf import settings
from tensorflow.keras.preprocessing import image

# Load the trained model once with the correct path
model_path = r'C:\Fruit_Identification_Using_Convolutional_Neural_Network\fruit_cnn_model.h5'
model = tf.keras.models.load_model(model_path)
# Set image size
IMG_SIZE = 100

# Load class labels
train_dir = os.path.join(settings.BASE_DIR, 'media', 'Fruit-Images-Dataset-master', 'Fruit-Images-Dataset-master', 'Training')
class_labels = sorted([d for d in os.listdir(train_dir) if os.path.isdir(os.path.join(train_dir, d))])




# import os
# import numpy as np
# import tensorflow as tf
# from django.shortcuts import render
# from django.core.files.storage import default_storage
# from django.conf import settings
# from tensorflow.keras.preprocessing import image

# def prediction(request):
#     context = {}
#     if request.method == 'POST' and request.FILES.get('image'):
#         uploaded_file = request.FILES['image']
        
#         # Construct the file path correctly using os.path.join
#         file_name = uploaded_file.name
#         file_path = os.path.join('uploads', file_name)

#         # Save the file to the media folder
#         full_file_path = default_storage.save(file_path, uploaded_file)
#         full_path = os.path.join(settings.MEDIA_ROOT, full_file_path)

#         try:
#             # Load and preprocess the image
#             img = image.load_img(full_path, target_size=(IMG_SIZE, IMG_SIZE))
#             img_array = image.img_to_array(img) / 255.0
#             img_array = np.expand_dims(img_array, axis=0)

#             # Make prediction
#             prediction = model.predict(img_array)
#             predicted_index = np.argmax(prediction)
#             predicted_label = class_labels[predicted_index]  # Map index to label

#             # Set the result in context
#             context['prediction'] = predicted_label
#             context['image_url'] = os.path.join(settings.MEDIA_URL, full_file_path)

#         except Exception as e:
#             context['error'] = f"Error during prediction: {str(e)}"

#     return render(request, 'users/prediction.html', context)


# import os
# import numpy as np
# import tensorflow as tf
# from django.shortcuts import render
# from django.core.files.storage import default_storage
# from django.conf import settings
# from tensorflow.keras.preprocessing import image

# # Set image size
# IMG_SIZE = 100

# # Assuming `model` and `class_labels` are loaded properly before this view
# def prediction(request):
#     context = {}
#     if request.method == 'POST' and request.FILES.get('image'):
#         uploaded_file = request.FILES['image']
        
#         # Save the uploaded file
#         file_name = uploaded_file.name
#         file_path = os.path.join('uploads', file_name)
#         full_file_path = default_storage.save(file_path, uploaded_file)
#         full_path = os.path.join(settings.MEDIA_ROOT, full_file_path)

#         try:
#             # Load and preprocess the image correctly (resize and normalize as during training)
#             img = image.load_img(full_path, target_size=(IMG_SIZE, IMG_SIZE))  # Ensure same image size
#             img_array = image.img_to_array(img) / 255.0  # Normalize as during training
#             img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

#             # Make prediction
#             prediction = model.predict(img_array)

#             # Get predicted class
#             predicted_index = np.argmax(prediction)  # Get the index of the class with highest probability
#             predicted_label = class_labels[predicted_index]  # Retrieve the class label

#             # Confidence of the prediction
#             confidence = np.max(prediction) * 100  # Get the confidence as a percentage

#             # Set context for rendering
#             context['prediction'] = predicted_label
#             context['confidence'] = f"{confidence:.2f}%"  # Display confidence score
#             context['image_url'] = os.path.join(settings.MEDIA_URL, full_file_path)

#         except Exception as e:
#             context['error'] = f"Error during prediction: {str(e)}"

#     return render(request, 'users/prediction.html', context)

# import os
# import numpy as np
# import tensorflow as tf
# from django.shortcuts import render
# from django.core.files.storage import default_storage
# from django.conf import settings
# from tensorflow.keras.preprocessing import image
# from PIL import Image
# from scipy.stats import entropy


# IMG_SIZE = 100


# ENTROPY_THRESHOLD = 0.5  



# def prediction(request):
#     context = {}
#     if request.method == 'POST' and request.FILES.get('image'):
#         uploaded_file = request.FILES['image']
      
#         file_name = uploaded_file.name
#         file_path = os.path.join('uploads', file_name)
#         full_file_path = default_storage.save(file_path, uploaded_file)
#         full_path = os.path.join(settings.MEDIA_ROOT, full_file_path)

#         try:
           
#             img = Image.open(full_path)
#             img.close() 

          
#             img = image.load_img(full_path, target_size=(IMG_SIZE, IMG_SIZE))
#             img_array = image.img_to_array(img)
            
          
#             img_array = img_array / 255.0 
#             img_array = np.expand_dims(img_array, axis=0)  

         
#             prediction = model.predict(img_array)[0]  
#             predicted_index = np.argmax(prediction)

        
#             pred_entropy = entropy(prediction)

        
#             if pred_entropy > ENTROPY_THRESHOLD:
#                 context['prediction'] = "Invalid"
#             else:
               
#                 predicted_label = class_labels[predicted_index]
#                 context['prediction'] = predicted_label

          
#             context['image_url'] = os.path.join(settings.MEDIA_URL, full_file_path)

#         except Image.UnidentifiedImageError:
#             context['message'] = "The uploaded file is not a valid image. Please upload an image file (e.g., JPG, PNG)."
#         except Exception as e:
#             context['message'] = "An error occurred while processing the image. Please try again."
#         finally:
          
#             pass

#     return render(request, 'users/prediction.html', context)



import os
import numpy as np
import tensorflow as tf
import imagehash
from PIL import Image
from django.shortcuts import render
from django.core.files.storage import default_storage
from django.conf import settings
from tensorflow.keras.preprocessing import image
from scipy.stats import entropy
import pickle

# Load known fruit image hashes
with open(os.path.join(settings.BASE_DIR, 'known_hashes.pkl'), 'rb') as f:
    known_hashes = pickle.load(f)

# Parameters
IMG_SIZE = 100
ENTROPY_THRESHOLD = 0.5
HASH_DISTANCE_THRESHOLD = 10  # Adjust based on similarity level

def is_similar_to_known_fruit(img_path):
    """Function to check if the uploaded image hash matches any known fruit image hash."""
    try:
        img = Image.open(img_path)
        test_hash = imagehash.average_hash(img)
        for known_hash in known_hashes:
            if abs(test_hash - known_hash) <= HASH_DISTANCE_THRESHOLD:
                return True
    except Exception as e:
        pass
    return False

def prediction(request):
    context = {}
    if request.method == 'POST' and request.FILES.get('image'):
        uploaded_file = request.FILES['image']
        
        # Save the uploaded file
        file_name = uploaded_file.name
        file_path = os.path.join('uploads', file_name)
        full_file_path = default_storage.save(file_path, uploaded_file)
        full_path = os.path.join(settings.MEDIA_ROOT, full_file_path)

        try:
            # Step 1: Validate if file is an image
            img = Image.open(full_path)
            img.close()

            # Step 2: Check if the image hash matches any known fruit image
            if not is_similar_to_known_fruit(full_path):
                context['prediction'] = "Invalid (Unknown or unrelated image)"
                context['image_url'] = os.path.join(settings.MEDIA_URL, full_file_path)
                return render(request, 'users/prediction.html', context)

            # Step 3: Preprocess for CNN model prediction
            img = image.load_img(full_path, target_size=(IMG_SIZE, IMG_SIZE))
            img_array = image.img_to_array(img) / 255.0  # Normalize to [0, 1]
            img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

            # Step 4: Make prediction using the trained model
            prediction_probs = model.predict(img_array)[0]
            pred_entropy = entropy(prediction_probs)

            # Step 5: Check the entropy of the prediction (uncertain predictions)
            if pred_entropy > ENTROPY_THRESHOLD:
                context['prediction'] = "Invalid (Uncertain prediction)"
            else:
                predicted_index = np.argmax(prediction_probs)
                predicted_label = class_labels[predicted_index]
                context['prediction'] = predicted_label

            # Include image URL for display
            context['image_url'] = os.path.join(settings.MEDIA_URL, full_file_path)

        except Image.UnidentifiedImageError:
            context['message'] = "The uploaded file is not a valid image. Please upload a JPG or PNG."
        except Exception as e:
            context['message'] = f"An error occurred: {str(e)}"

    return render(request, 'users/prediction.html', context)
