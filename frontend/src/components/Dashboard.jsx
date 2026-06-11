
import React, { useEffect, useState } from "react";
import axios from "axios";
import { jsPDF } from "jspdf";

function Dashboard() {

  const [stats, setStats] = useState({});
  const [history, setHistory] = useState([]);

  useEffect(() => {

    loadDashboard();
    loadHistory();

  }, []);

  const loadDashboard = async () => {

    const response = await axios.get(
      "http://127.0.0.1:8000/api/dashboard/"
    );

    setStats(response.data);
  };

  const loadHistory = async () => {

    const response = await axios.get(
      "http://127.0.0.1:8000/api/history/"
    );

    setHistory(response.data);
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
      `report_${item.id}.pdf`
    );
  };

  return (

    <div className="container py-5">

      <h1 className="text-center mb-4">
        Dashboard
      </h1>

      <div className="row">

        <div className="col-md-4 mb-3">

          <div className="card shadow text-center">

            <div className="card-body">

              <h5>Total Scans</h5>

              <h2>
                {stats.total_scans}
              </h2>

            </div>

          </div>

        </div>

        <div className="col-md-4 mb-3">

          <div className="card shadow text-center">

            <div className="card-body">

              <h5>Healthy Plants</h5>

              <h2>
                {stats.healthy_plants}
              </h2>

            </div>

          </div>

        </div>

        <div className="col-md-4 mb-3">

          <div className="card shadow text-center">

            <div className="card-body">

              <h5>Diseased Plants</h5>

              <h2>
                {stats.diseased_plants}
              </h2>

            </div>

          </div>

        </div>

      </div>

      <div className="card shadow mt-4">

        <div className="card-body">

          <h4 className="mb-3">
            Prediction History
          </h4>

          <table className="table table-bordered">

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

  );
}

export default Dashboard;

