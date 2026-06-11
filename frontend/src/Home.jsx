
import React, { useState } from "react";
import axios from "axios";
import "./Home.css";

function Home() {

  const [image, setImage] = useState(null);
  const [preview, setPreview] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleImageChange = (e) => {

    const file = e.target.files[0];

    setImage(file);

    if (file) {
      setPreview(URL.createObjectURL(file));
      setResult(null);
    }
  };

  const handlePredict = async () => {

    if (!image) {
      alert("Please select an image");
      return;
    }

    setLoading(true);

    const formData = new FormData();
    formData.append("image", image);

    try {

      const response = await axios.post(
        "http://127.0.0.1:8000/api/predict/",
        formData
      );

      setResult(response.data);

    } catch (error) {

      console.error(error);
      alert("Prediction failed");

    } finally {

      setLoading(false);
    }
  };

  const getPlantName = () => {

    if (!result?.disease) return "";

    const plant = result.disease.split("___")[0];

    const plantNames = {
      "Pepper__bell": "Bell Pepper",
      "Potato": "Potato",
      "Tomato": "Tomato"
    };

    return plantNames[plant] || plant;
  };

  const getDiseaseName = () => {

    if (!result?.disease) return "";

    const parts = result.disease.split("___");

    if (parts.length > 1) {
      return parts[1]
        .split("_")
        .join(" ");
    }

    return result.disease;
  };

  return (

    <div className="main-container">

      <div className="container">

        <div className="row justify-content-center">

          <div className="col-lg-8">

            <div className="glass-card">

              <h1 className="title text-center">
                🌿 Plant Disease Detection
              </h1>

              <p className="subtitle text-center">
                AI Powered Crop Health Analysis
              </p>

              <input
                type="file"
                className="form-control upload-input"
                onChange={handleImageChange}
              />

              {preview && (

                <div className="preview-container">

                  <img
                    src={preview}
                    alt="Leaf Preview"
                    className="preview-image"
                  />

                </div>

              )}

              <div className="text-center mt-4">

                <button
                  className="btn btn-success modern-btn"
                  onClick={handlePredict}
                  disabled={loading}
                >
                  {loading
                    ? "Analyzing..."
                    : "Predict Disease"}
                </button>

                <a
                  href="/dashboard"
                  className="btn btn-primary modern-btn ms-3"
                >
                  Dashboard
                </a>

              </div>

              {result && (

                <div className="result-card mt-4">

                  <h3 className="text-success mb-3">
                    Prediction Result
                  </h3>

                  <div className="row">

                    <div className="col-md-6">

                      <div className="info-card">

                        <h5>🌱 Plant</h5>

                        <p>
                          {getPlantName()}
                        </p>

                      </div>

                    </div>

                    <div className="col-md-6">

                      <div className="info-card">

                        <h5>🦠 Disease</h5>

                        <p>
                          {getDiseaseName()}
                        </p>

                      </div>

                    </div>

                  </div>

                  <div className="mt-4">

                    <h5>
                      Confidence Score
                    </h5>

                    <div
                      className="progress"
                      style={{
                        height: "30px",
                        borderRadius: "20px"
                      }}
                    >

                      <div
                        className="progress-bar progress-bar-striped progress-bar-animated bg-success"
                        role="progressbar"
                        style={{
                          width: `${result.confidence}%`
                        }}
                      >
                        {result.confidence}%
                      </div>

                    </div>

                  </div>

                  <div className="alert alert-info mt-4">

                    <h5>
                      📖 Description
                    </h5>

                    <p className="mb-0">
                      {result.description}
                    </p>

                  </div>

                  <div className="alert alert-warning">

                    <h5>
                      💊 Treatment Recommendation
                    </h5>

                    <p className="mb-0">
                      {result.treatment}
                    </p>

                  </div>

                </div>

              )}

            </div>

          </div>

        </div>

      </div>

    </div>

  );
}

export default Home;

