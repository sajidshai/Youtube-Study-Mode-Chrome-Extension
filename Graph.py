
import matplotlib.pyplot as plt
import io
import base64
import numpy as np

def generate(data):
        
    pos_count = data.count('Positive')
    neg_count = data.count('Negative')
    neu_count = data.count('Neutral')

    # Labels and sizes for the pie chart
    labels = ['positive', 'negative', 'neutral']
    sizes = [pos_count, neg_count, neu_count]

    # Create a pie chart
    plt.figure(figsize=(8, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title('Sentiment Results')
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Add a legend to the graph
    plt.legend()

    # Display the graph
    plt.tight_layout()
        # Save the plot to a bytes buffer
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    # Encode the image in base64 to send to the template
    graph = base64.b64encode(image_png).decode('utf-8')

    # Close the plot
    plt.close()
    #plt.show()

    return graph


    
if __name__ == '__main__':
    generate(['positive', 'positive','negative', 'negative'])