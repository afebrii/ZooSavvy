package com.afebrii.zoosavvy.ui.main

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.afebrii.zoosavvy.R
import com.afebrii.zoosavvy.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {
    private lateinit var binding: ActivityMainBinding
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        // Andika Febriansyah
    }
}