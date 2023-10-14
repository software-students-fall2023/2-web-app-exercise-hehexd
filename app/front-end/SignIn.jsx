import React from "react";
import "./style.css";

export const SignIn = () => {
  return (
    <div className="SIGN-IN">
      <div className="forgot-password-sign">
        <div className="overlap-group">
          <div className="text-wrapper">Forgot Password</div>
        </div>
      </div>
      <div className="sign-in-button">
        <div className="overlap-group">
          <div className="text-wrapper">Sign in</div>
        </div>
      </div>
      <div className="PASSWORD-sign-in">
        <div className="overlap">
          <div className="div">[PASSWORD]</div>
        </div>
      </div>
      <div className="EMAIL-sign-in">
        <div className="overlap">
          <div className="text-wrapper-2">[EMAIL]</div>
        </div>
      </div>
      <div className="overlap-2">
        <div className="create-account">
          <div className="overlap-group">
            <div className="text-wrapper-3">Create Account</div>
          </div>
        </div>
        <div className="text-wrapper-4">Create Account</div>
      </div>
      <div className="text-wrapper-5">Budget Tracker</div>
    </div>
  );
};
