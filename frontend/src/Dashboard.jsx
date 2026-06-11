
import React, { useEffect, useState } from "react";
import axios from "axios";
import { jsPDF } from "jspdf";

function Dashboard() {

  const [stats, setStats] = useState({
    total_scans: 0,
    healthy_plants: 0,
    diseased_plants: 0
  });

  const [history, setHistory] = useState([]);

  useEffect(() => {

    fetchDashboard();
    fetchHistory();

  }, []);

  const fetchDashboard = async () => {

    try {

      const response = await axios.get(
        "http://127.0.0.1:8000/api/dashboard/"
      );

      setStats(response.data);

    } catch (error) {

      console.error(error);
    }
  };

  const fetchHistory = async () => {

    try {

      const response = await axios.get(
        "http://127.0.0.1:8000/api/history/"
      );

      setHistory(response.data);

    } catch (error) {

      console.error(error);
    }
  };

  const downloadPDF = (item) => {

    const doc = new jsPDF();

    doc.setFontSize(18);
    doc.text(
      "Plant Disease Detection Report",
      20,
      20
    );

    doc.setFontSize(12);

    doc.text(
      `Disease: ${item.disease}`,
      20,
      40
    );

    doc.text(
      `Confidence: ${item.confidence}%`,
      20,
      55
    );

    doc.text(
      `Date: ${item.timestamp}`,
      20,
      70
    );

    doc.save(
      `prediction_${item.id}.pdf`
    );
  };

  return (

    <div className="container py-5">

      <h1 className="text-center mb-4">
        Plant Analytics Dashboard
      </h1>

      <div className="row">

        <div className="col-md-4 mb-3">

          <div className="card shadow border-0">

            <div className="card-body text-center">

              <h5>Total Scans</h5>

              <h2 className="text-primary">
                {stats.total_scans}
              </h2>

            </div>

          </div>

        </div>

        <div className="col-md-4 mb-3">

          <div className="card shadow border-0">

            <div className="card-body text-center">

              <h5>Healthy Plants</h5>

              <h2 className="text-success">
                {stats.healthy_plants}
              </h2>

            </div>

          </div>

        </div>

        <div className="col-md-4 mb-3">

          <div className="card shadow border-0">

            <div className="card-body text-center">

              <h5>Diseased Plants</h5>

              <h2 className="text-danger">
                {stats.diseased_plants}
              </h2>

            </div>

          </div>

        </div>

      </div>

      <div className="card shadow border-0 mt-4">

        <div className="card-body">

          <h3 className="mb-3">
            Prediction History
          </h3>

          <div className="table-responsive">

            <table className="table table-striped">

              <thead>

                <tr>

                  <th>ID</th>
                  <th>Disease</th>
                  <th>Confidence</th>
                  <th>Date</th>
                  <th>PDF</th>

                </tr>

              </thead>

              <tbody>

                {history.map((item) => (

                  <tr key={item.id}>

                    <td>{item.id}</td>

                    <td>{item.disease}</td>

                    <td>{item.confidence}%</td>

                    <td>{item.timestamp}</td>

                    <td>

                      <button
                        className="btn btn-success btn-sm"
                        onClick={() =>
                          downloadPDF(item)
                        }
                      >
                        Download
                      </button>

                    </td>

                  </tr>

                ))}

              </tbody>

            </table>

          </div>

        </div>

      </div>

      <div className="text-center mt-4">

        <a
          href="/"
          className="btn btn-primary"
        >
          Back to Prediction
        </a>

      </div>

    </div>

  );
}

export default Dashboard;

