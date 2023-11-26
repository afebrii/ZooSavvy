package com.afebrii.zoosavvy.ui.signup

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.afebrii.zoosavvy.R
import com.afebrii.zoosavvy.databinding.ActivitySignupBinding
import com.afebrii.zoosavvy.ui.signin.SigninActivity

class SignupActivity : AppCompatActivity() {
    private lateinit var binding: ActivitySignupBinding
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivitySignupBinding.inflate(layoutInflater)
        setContentView(binding.root)

        binding.loginHereButton.setOnClickListener {
            val i = Intent(this, SigninActivity::class.java)
            startActivity(i)
            finish()
        }
    }
}