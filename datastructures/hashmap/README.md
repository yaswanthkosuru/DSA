# HashMap Overview

## Introduction

A **HashMap** is a data structure that provides an efficient way to store and retrieve data using key-value pairs. It is based on the concept of **hashing**, where a hash function is used to compute an index (or hash code) into an array, in which the desired value can be found or stored.

## Key Characteristics

- **Key-Value Pairs**: Each element in a HashMap is stored as a pair consisting of a key and a value.
- **Hash Function**: A function that converts the key into a hash code, which is then mapped to an index in the underlying array.
- **No Duplicate Keys**: Each key in the HashMap is unique, but different keys can map to the same value.
- **Unordered**: The order of elements in a HashMap is not guaranteed to be in the same order as insertion. HashMaps are not sorted.

## Basic Operations

- **Insertion (`put`)**: Adds a new key-value pair to the HashMap. If the key already exists, the value is updated.
- **Lookup (`get`)**: Retrieves the value associated with a given key.
- **Deletion (`remove`)**: Removes the key-value pair associated with the given key.
- **Contains Key (`containsKey`)**: Checks if a particular key exists in the HashMap.
- **Size (`size`)**: Returns the number of key-value pairs in the HashMap.

## HashMap Structure

A HashMap internally uses an array of linked lists (or trees in some cases) to store data. Each key is processed by a hash function to determine its index in the array:

- **Buckets**: The array slots (or "buckets") where the key-value pairs are stored.
- **Collisions**: Occur when two keys map to the same bucket. These are typically resolved using linked lists or balanced binary trees.
